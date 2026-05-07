from dotenv import load_dotenv
import os

load_dotenv()

# ======================
# DATABASE
# ======================
DATABASE_URL = os.getenv("postgresql://fixit_dbs_wu7y_user:z3h2Pf5HVEwvfPi1nWTYmCcheQ4Qn9rm@dpg-d7ufji3eo5us73e18p6g-a/fixit_dbs_wu7y")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set!")


# ======================
# SECURITY
# ======================
SECRET_KEY = os.getenv("fixit_super_secret_key_2026_secure_backend")
if not SECRET_KEY:
    raise ValueError("❌ SECRET_KEY is not set!")

ALGORITHM = os.getenv("ALGORITHM", "HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
)


# ======================
# PAYSTACK
# ======================
PAYSTACK_SECRET = os.getenv("PAYSTACK_SECRET")
if not PAYSTACK_SECRET:
    print("⚠️ WARNING: PAYSTACK_SECRET not set (payments will fail)")