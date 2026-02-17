from defect_detection import detect_defects
from database import init_db, save_scan

def main():
    init_db()

    image_path = input("Enter wafer image path: ")

    defects = detect_defects(image_path)

    save_scan(image_path, defects)

    print(f"Defects detected: {defects}")
    print("Scan saved to database.")

if __name__ == "__main__":
    main()
