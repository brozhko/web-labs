from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Client(db.Model):
    __tablename__ = "clients"

    client_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100))
    passport = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)

    accounts = db.relationship("Account", back_populates="client")
    logins = db.relationship("LoginHistory", back_populates="client")


class Currency(db.Model):
    __tablename__ = "currencies"

    currency_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), unique=True, nullable=False)
    name = db.Column(db.String(50))

    accounts = db.relationship("Account", back_populates="currency")


class Bank(db.Model):
    __tablename__ = "banks"

    bank_id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(100), nullable=False)
    mfo = db.Column(db.String(6), unique=True, nullable=False)

    accounts = db.relationship("Account", back_populates="bank")
    recipients = db.relationship("Recipient", back_populates="bank")


class Account(db.Model):
    __tablename__ = "accounts"

    account_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.client_id"))
    bank_id = db.Column(db.Integer, db.ForeignKey("banks.bank_id"))
    currency_id = db.Column(db.Integer, db.ForeignKey("currencies.currency_id"))
    account_number = db.Column(db.String(20), unique=True)
    balance = db.Column(db.Numeric(15, 2), default=0)
    opened_at = db.Column(db.DateTime)

    client = db.relationship("Client", back_populates="accounts")
    bank = db.relationship("Bank", back_populates="accounts")
    currency = db.relationship("Currency", back_populates="accounts")

    cards = db.relationship("Card", back_populates="account")

    outgoing_transactions = db.relationship(
        "Transaction",
        foreign_keys="Transaction.from_account",
        back_populates="from_acc",
    )
    incoming_transactions = db.relationship(
        "Transaction",
        foreign_keys="Transaction.to_account",
        back_populates="to_acc",
    )


class Card(db.Model):
    __tablename__ = "cards"

    card_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    card_number = db.Column(db.String(16), unique=True)
    expiry_date = db.Column(db.Date)
    cvv = db.Column(db.String(3))

    account = db.relationship("Account", back_populates="cards")


class PaymentType(db.Model):
    __tablename__ = "payment_types"

    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(100))

    payments = db.relationship("Payment", back_populates="type")


class Recipient(db.Model):
    __tablename__ = "recipients"

    recipient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    iban = db.Column(db.String(34))
    bank_id = db.Column(db.Integer, db.ForeignKey("banks.bank_id"))

    bank = db.relationship("Bank", back_populates="recipients")
    payments = db.relationship("Payment", back_populates="recipient")


class Payment(db.Model):
    __tablename__ = "payments"

    payment_id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey("payment_types.type_id"))
    recipient_id = db.Column(db.Integer, db.ForeignKey("recipients.recipient_id"))
    amount = db.Column(db.Numeric(15, 2))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)

    type = db.relationship("PaymentType", back_populates="payments")
    recipient = db.relationship("Recipient", back_populates="payments")
    transactions = db.relationship("Transaction", back_populates="payment")


class Transaction(db.Model):
    __tablename__ = "transactions"

    transaction_id = db.Column(db.Integer, primary_key=True)
    from_account = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    to_account = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    payment_id = db.Column(db.Integer, db.ForeignKey("payments.payment_id"))
    amount = db.Column(db.Numeric(15, 2))
    date_time = db.Column(db.DateTime)
    status = db.Column(db.Enum("pending", "completed", "failed"), default="completed")

    from_acc = db.relationship(
        "Account",
        foreign_keys=[from_account],
        back_populates="outgoing_transactions",
    )
    to_acc = db.relationship(
        "Account",
        foreign_keys=[to_account],
        back_populates="incoming_transactions",
    )
    payment = db.relationship("Payment", back_populates="transactions")


class LoginHistory(db.Model):
    __tablename__ = "login_history"

    log_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.client_id"))
    login_time = db.Column(db.DateTime)
    ip_address = db.Column(db.String(50))

    client = db.relationship("Client", back_populates="logins")
