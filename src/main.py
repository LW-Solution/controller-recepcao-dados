import sub

def main():
    message, topic = sub.conectar_sub()
    print("PayLoad: ", message)
    print("Topic: ", topic)

if __name__ == "__main__":
    main()