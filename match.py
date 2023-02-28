server_response = 404

match server_response:
    case 404:
        print("Not Found")
    case 200:
        print("OK")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Error")

