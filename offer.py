import pandas as pd
userOffers = pd.read_csv('offers.csv');
userOffers.head();
#get list of unique customer
offerList=list(set(userOffers["offerId"].tolist()));

#Get count of users
userCount=len(set(userOffers["offerId"].tolist()))

#Create an empty data frame to store item affinity scores for items.
itemAffinity= pd.DataFrame(columns=('offer1', 'offer2', 'score'))
rowCount=0
#print(itemAffinity);
#For each item in the list, compare with other items.

for ind1 in range(len(offerList)):
#Get list of users who bought this item 1.
    item1Users = userOffers[userOffers.offerId == offerList[ind1]]['userId'].tolist();
   # print("IteM 1",item1Users);

    for ind2 in range(ind1, len(offerList)):
        if ( ind1 == ind2):
            continue
        #Get list of users who bought item 2
        item2Users=userOffers[userOffers.offerId==offerList[ind2]]['userId'].tolist()
         #print("Item 2",item2Users)

         #Find score. Find the common list of users and divide it by the total users.
        commonUsers= len(set(item1Users).intersection(set(item2Users)))
        score=commonUsers / userCount
         #print("Score",score)

        #Add a score for item 1, item 2
        itemAffinity.loc[rowCount] = [offerList[ind1],offerList[ind2],score]
        rowCount +=1
        #Add a score for item2, item 1. The same score would apply irrespective of the sequence.
        itemAffinity.loc[rowCount] = [offerList[ind2],offerList[ind1],score]
        rowCount +=1


#Check final result
itemAffinity.head()
print(itemAffinity)

searchItem=5006
recoList=itemAffinity[itemAffinity.offer1==searchItem]\
        [["offer2","score"]]\
        .sort_values("score", ascending=[0])

print("Recommendations for item 5001\n", recoList)








