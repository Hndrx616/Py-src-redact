'''
author Stephen Hilliard (c) 2016.
developer Stephen Hilliard (c) 2016.
'''
import httplib
from xml.dom.minidom import parse, parseString, Node

devKey = 'developerkey'
appKey = 'applicationkey'
certKey = 'certificatekey'
userToken = 'token'
serverUrl = 'api.ebay.com'

def getHeaders(apicall,siteID="0",compatabilityLevel = "433"):
	headers = {"X-EBAY-API-COMPATIBILITY-LEVEL": compatabilityLevel,
			   "X-EBAY-API-DEV-NAME": devKey,
			   "X-EBAY-API-APP-NAME": appKey,
			   "X-EBAY-API-CERT-NAME": certKey,
			   "X-EBAY-API-CALL-NAME": apicall,
			   "X-EBAY-API-SITEID": siteID,
			   "Content-Type": "test/xml"}
	return headers

def sendRequest(apicall,xmlparameters):
	connection = httplib.HTTPSConnection(serverUrl)
	connection.request("POST", '/ws/api.dll', xmlparameters,getHeaders(apicall))
	response = connection.getresponse()
	if response.status != 200:
		print "Error sending request:" + response.reason
	else:
		data = response.read()
		connection.close()
	return data

def setSingleValue(node,tag):
	nl=node.getElementByTagName(tag)
	if len(nl)>0:
		tagNode=nl[0]
		if tagNode.hasChildNode():
			return tagNode.firstChild.nodeValue
	return '-1'

def doSearch(query,categoryID=None,page=1):
	xml = "<?xml version='1.0' encoding='utf-8'?>"+\
		  "<GetSearchResultsRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
		  "<RequesterCredentials><ebayAuthToken>" +\
		  userToken +\
		  "</eBayAuthtoken></RequesterCredentials>" + \
		  "<Pagination>"+\
		  	"<EntriesPerPage>200</EntriesPerPage>"+\
		  	"<PageNumber>"+str(page)+"</PageNumber>"+\
		  "</Pagination>"+\
		  "<Query>" + query + "</Query>"
	if categoryID!=None:
		xml+="<CategoryID>"+str(categoryID)+"</CategoryID>"
	xml+="</GetSearchReultsRequest>"

	data=sendRequest('GetSearchResults',xml)
	response = parseString(data)
	itemNodes = response.getElementByTagName('Item');
	results = []
	for item in itemNodes:
		itemID=getSingleValue(item,'ItemID')
		itemTItle=getSingleValue(item,'Title')
		itemPrice=getSingleValue(item,'CurrentPrice')
		itemEnds=getSingleValue(item,'EndTime')
		results.append((itemId,itemTitle,itemPrice,itemEnds))
	return results

def getCategory(query='',parentID=None,siteID='0'):
	lquery=query.lower()
	xml = "<?xml version='1.0' encoding='utf-8'?>"+\
		  "<GetCategoriesRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
		  "<RequesterCredentials><ebayAuthToken>" +\
		  userToken +\
		  "</eBayAuthtoken></RequesterCredentials>"+\
		  "<DetailLevel>ReturnAll</DetailLavel>"+\
		  "<ViewAllNodes>true</ViewAllNodes>"+\
		  "<CategorySiteID>"+siteID+"</CategorySiteID>"
	if parentID==None:
		xml+="<LevelLimit>1</LevelLimit>"
	else:
		xml+="<CategoryParent>"+str(parentID)+"</CategoryParent>"
	xml += "</GetCategoriesRequest>"
	data=sendRequest('GetCategories',xml)
	categoryList=parseString(data)
	catNodes=categoryList.getElementByTagName('Category')
	for node in catNodes:
		catid=getSingleValue(node,'CategoryID')
		name=getSingleValue(node,'CategoryName')
		if name.lower().find(lquery)!=-1:
			print catid,name

def getItem(itemID):
	xml = "<?xml version='1.0' encoding='utf-8'?>"+\
		  "<GetItemRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
		  "<RequesterCredentials><ebayAuthToken>" +\
		  userToken +\
		  "</eBayAuthtoken></RequesterCredentials>" + \
		  "<ItemID>" + str(itemID) + "</ItemID>"+\
		  "<DetailLevel>ItemReturnAttributes</DetailLevel>"+\
		  "</GetItemRequest>"
	data=sendRequest('GetItem',xml)
	result={}
	response=parseString(data)
	result['title']=getSingleValue(response,'Title')
	sellingStatusNode = response.getElementByTagName('SellingStatus')[0];
	result['price']=getSingleValue(sellingStatusNode,'CurrentPrice')
	result['bids']=getSingleValue(sellingStatusNode,'BidCount')
	seller = response.getElementByTagName('Seller')
	result['feedback'] = getSingleValue(seller[0],'FeedbackScore')
	attributeSet=response.getElementByTagName('Attribute');
	attributes={}
	for att in attributeSet:
		attID=att.attributes.getNamedItem('attributeID').nodeValue
		attValue=getSingleValue(att,'ValueLiteral')
		attributes[attID]=attValue
	result['attributes']=attributes
	return result