# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

# print("Creating limiter...")

# limiter = Limiter(
#     key_func=get_remote_address,
#     default_limits=["1000 per day", "100 per hour"],
#     storage_uri="memory://"
# )