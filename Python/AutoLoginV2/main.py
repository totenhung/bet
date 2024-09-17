import loginGroup as lgr
import login78 as l78
import loginJun as lju
import loginMb as lmb

def main():
    driver = lgr.create_chrome_driver(detach=True)
    try:
        l78.login78(driver)
        lju.loginJun(driver)
        lmb.loginMb(driver)
        lgr.loginGroup(driver)
    finally:
        pass

if __name__ == "__main__":
    main()