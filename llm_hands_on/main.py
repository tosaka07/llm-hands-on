import uvicorn


def main() -> None:
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=5555,
    )


if __name__ == "__main__":
    print("Starting the application")
    main()
