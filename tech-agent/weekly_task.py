from app import run_agent

if __name__ == "__main__":
    print("Weekly Tech Agent started...")

    try:
        summary = run_agent()
        print("Email sent successfully!")
        print(summary)

    except Exception as error:
        print(f"Weekly Agent failed: {error}")
        raise
