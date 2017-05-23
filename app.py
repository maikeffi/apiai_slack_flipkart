import requests
import json

fkAffiliateId = "******"
fkAffiliateToken = "*****"

#url = "https://affiliate-api.flipkart.net/affiliate/search/json"
url = "https://affiliate-api.flipkart.net/affiliate/api/" + fkAffiliateId + ".json";
#url = "https://affiliate-api.flipkart.net/affiliate/1.0/feeds/uve2payle/category/ckf-czl.json?expiresAt=1495512790980&sig=7dd254b047f571a027b2b6884ad0eb39"
#urlv1 = "https://affiliate-api.flipkart.net/affiliate/1.0/search.json?query={productString}&resultCount={count}"
#product = "Sony GTK-N1BT Mini Hi-Fi System(Black)"
#count = "1"

header = {"Fk-Affiliate-Id":fkAffiliateId,"Fk-Affiliate-Token":fkAffiliateToken}

#url = urlv1.replace("{productString}",product).replace("{count}",count)



r = requests.get(url,headers=header)
data = json.loads(r.text)

#print(r.json())
listing = data['apiGroups']['affiliate']['apiListings']
#for key in listing.keys():
#    print(key)

for list in listing.values():
    print("Catagory :"+list['availableVariants']['v1.1.0']['resourceName'] +" Url : "+list['availableVariants']['v1.1.0']['get'])
