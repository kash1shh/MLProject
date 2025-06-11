import sys
from src.logger import logging
# import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    error_message=(
        f"Error occurred in Python script name [{exc_tb.tb_frame.f_code.co_filename}] at line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        self.error_message = error_message_detail(error_msg, error_detail=error_detail)

    def __str__(self):
        return self.error_message

    # def __repr__(self) -> str:
    #     return CustomException.__name__.str()


if __name__=="__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys)