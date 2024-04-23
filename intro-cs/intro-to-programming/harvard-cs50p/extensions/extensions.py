file_name = input("File name: ").strip().lower()

parts = file_name.rsplit(".", maxsplit=1)
extension = parts[1] if len(parts) > 1 else ""

match extension:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
