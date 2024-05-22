import uvicorn


def main() -> None:
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=4598,
    )


if __name__ == "__main__":
    print("Starting the application")
    main()
