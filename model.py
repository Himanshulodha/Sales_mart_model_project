import pickle

Item_Type={4: 'Dairy',
 14: 'Soft Drinks',
 10: 'Meat',
 6: 'Fruits and Vegetables',
 9: 'Household',
 0: 'Baking Goods',
 13: 'Snack Foods',
 5: 'Frozen Foods',
 2: 'Breakfast',
 8: 'Health and Hygiene',
 7: 'Hard Drinks',
 3: 'Canned',
 1: 'Breads',
 15: 'Starchy Foods',
 11: 'Others',
 12: 'Seafood'}

Item_Fat_Content={0: 'Low Fat', 2: 'Regular', 1: 'Non-Edible'}
Outlet_Size = {1: 'Medium', 2: 'Small', 0: 'High'}
Outlet_Location_Type = {0: 'Tier 1', 2: 'Tier 3', 1: 'Tier 2'}
Outlet_Type = {1: 'Supermarket Type1',
 2: 'Supermarket Type2',
 0: 'Grocery Store',
 3: 'Supermarket Type3'}

New_Item_Type = {1: 'Food', 0: 'Drinks', 2: 'Non-Consumable'}
Outlet_Identifier={9: 'OUT049',
 3: 'OUT018',
 0: 'OUT010',
 1: 'OUT013',
 5: 'OUT027',
 7: 'OUT045',
 2: 'OUT017',
 8: 'OUT046',
 6: 'OUT035',
 4: 'OUT019'}

def find(st,dic):
    for key in dic.keys():
        if dic[key]==st:
            return key
        return 0

def Predict_Sales(li):
    li[0]=float(li[0])
    li[1]=find(li[1],Item_Fat_Content)
    li[2]=float(li[2])
    li[3]=find(li[5],Item_Type) 
    li[4]=float(li[4])
    li[5]=find(li[5],Outlet_Size)
    li[6]=find(li[6],Outlet_Location_Type)
    li[7]=find(li[7],Outlet_Type)
    li[8]=find(li[8],New_Item_Type)
    li[9]=float(li[9])
    li[10]=find(li[10],Outlet_Identifier)

    pickled_model = pickle.load(open('Item_Outlet_Sales.pkl', 'rb'))
    print(li)
    k=pickled_model.predict([li])

    return k[0]