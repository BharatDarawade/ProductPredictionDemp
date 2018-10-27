import pandas as pd
userOffers = pd.read_csv('offers.csv');
userOffers.head();
#get list of unique customer
offerList=list(set(userOffers['optionBpId'].tolist()));

#Get count of users
userCount=len(set(userOffers['offerId'].tolist()))

#Create an empty data frame to store item affinity scores for items.
itemAffinity= pd.DataFrame(columns=('offer1', 'offer2', 'score'))
rowCount=0
#print(itemAffinity);
#For each item in the list, compare with other items.

for ind1 in range(len(offerList)):
#Get list of users who bought this item 1.
    offer1User = userOffers[userOffers.optionBpId == offerList[ind1]]['offerId'].tolist();
    print("IteM 1",offer1User);

    for ind2 in range(ind1, len(offerList)):
        if ( ind1 == ind2):
            continue
        #Get list of users who bought item 2
        offer2User=userOffers[userOffers.optionBpId==offerList[ind2]]['offerId'].tolist()
         #print("Item 2",offer2User)

         #Find score. Find the common list of users and divide it by the total users.
        commonUsers= len(set(offer1User).intersection(set(offer2User)))
        score=commonUsers / userCount
        print("Score",score)

        #Add a score for item 1, item 2
        itemAffinity.loc[rowCount] = [offerList[ind1],offerList[ind2],score]
        rowCount +=1
        #Add a score for item2, item 1. The same score would apply irrespective of the sequence.
        itemAffinity.loc[rowCount] = [offerList[ind2],offerList[ind1],score]
        rowCount +=1


#Check final result
itemAffinity.head()
print(itemAffinity)

searchItem=5001
recoList=itemAffinity[itemAffinity.offer1==searchItem]\
        [['offer2','score']]\
        .sort_values("score", ascending=[0])

print("Recommendations for item 5001\n", recoList)








