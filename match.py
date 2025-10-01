def http_error_msg(status):
    match status:
        case 400:
            return "bad request"
        case 404 :
            return "Not found"
        case 200:
            return "Success true ,status OK"
        case _ :
            return "Somethig wrong with your internet"
    
status_list  = [404,200,400,34454]

for status in status_list:
    print(f"Status : {status }  , message : {http_error_msg(status)}" )