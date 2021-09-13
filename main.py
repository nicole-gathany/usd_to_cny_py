def usdcny(usd):
    yuan = usd * 6.75
    dec = str(yuan).split(".")[1]
    
    if len(dec) == 1:
        return str(yuan) + "0 Chinese Yuan"
    else:
        return str(yuan) + " Chinese Yuan"