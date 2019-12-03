
# coding: utf-8

# In[1]:


# coding: utf-8

import json
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
import win32api

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
web3.eth.defaultAccount = web3.eth.accounts[0]
address = web3.toChecksumAddress('0x745f1a2C2c92f1e119830fc090b5Be3568d81C0E')

contract = web3.eth.contract(address= address, abi =[
	{
		"constant": False,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			},
			{
				"name": "coin",
				"type": "string"
			},
			{
				"name": "coinNum",
				"type": "string"
			},
			{
				"name": "value",
				"type": "uint256"
			},
			{
				"name": "isBought",
				"type": "bool"
			},
			{
				"name": "date",
				"type": "string"
			}
		],
		"name": "storeData",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			}
		],
		"name": "retrieveMyData_recent",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getDataLength",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			},
			{
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "retrieveMyData_index",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "retrieveArrData",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "key",
				"type": "string"
			}
		],
		"name": "getMyDataLength",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
])


# In[2]:


def typeCheck(data, _type):
    if str(type(data)) == f"<class '{_type}'>":
        return True
    return False


# In[3]:


def storeData(key, coin, coinNum, value, isBought, date) :
    
    if (
        typeCheck(key, "str") == True and   typeCheck(key, "str") ==True and
        typeCheck(key, "str") == True and   typeCheck(key, "str") ==True and
        typeCheck(key, "str") == True and   typeCheck(key, "str") ==True
    ) :        
        tx_hash = contract.functions.storeData(key, coin, coinNum,value, isBought,date).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        success = contract.functions.storeData(key, coin, coinNum,value, isBought,date).call()
        if success == True:
            win32api.MessageBox(0, f"데이터가 저장 되었습니다. coin : {coin},  coinNum : {coinNum}, date : {date}, isBought : {str(isBought)}, value : {value}", '알림창')
        else :
            win32api.MessageBox(0, f'데이터가 저장에 실패했습니다', '알림창')
    else :
        win32api.MessageBox(0, f'데이터 타입을 정확하게 입력해주세요.', '알림창')


# In[4]:


def retrieveMyData_recent(key) :
    tx_hash = contract.functions.retrieveMyData_recent(key).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    (_coin, _coinNum, _date, _isBought, _value) = contract.functions.retrieveMyData_recent(_id).call()
    return (_coin, _coinNum, _date, _isBought, _value)


# In[5]:


def retrieveMyData_index(key, index):
    tx_hash = contract.functions.retrieveMyData_index(key, index).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    (_coin, _coinNum, _date, _isBought, _value) = contract.functions.retrieveMyData_index(key, index).call()
    return (_coin, _coinNum, _date, _isBought, _value)


# In[6]:


def retrieveArrData(num) :
    tx_hash = contract.functions.retrieveArrData(num).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    (_id, _coin, _coinNum, _date, _isBought, _value) = contract.functions.retrieveArrData(num).call()
    return (_id, _coin, _coinNum, _date, _isBought, _value)


# In[7]:


def getMyDataLength(key):
    tx_hash = contract.functions.getMyDataLength(key).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    length = contract.functions.getMyDataLength(key).call()
    return length


# In[8]:


def getDataLength():
    tx_hash = contract.functions.getDataLength().transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    length = contract.functions.getDataLength().call()
    return length


# In[9]:


def showDataArr_Id(key, num):
    """ 나의 최근 num개 거래를 보여주기 위한 함수 """
    
    if (typeCheck(key, "str") == False or   typeCheck(num, "int") == False) :
        win32api.MessageBox(0, f'데이터 타입을 정확하게 입력해주세요.', '알림창')
        return
    length = getMyDataLength(key)
    if length == 0:
        win32api.MessageBox(0, '저장된 데이터가 없습니다.', '알림창')
        return
    if num > length:
        num = length
    wanted = length - num
    showMyData = retrieveMyData_index(key, length - 1)
    for i in range(length - 1, wanted - 1, -1):
        showMyData = showMyData + retrieveMyData_index(key, i)
        #retrieveArrData에서 한개씩 받아오면서 여기서 처리하던가 아니면 리턴 받은 모든 데이터를 처리하던가 
        #결정은 당신의 몫이오
    return showMyData


# In[10]:


def showDataArr(num):
   
    """ 전체 데이터에서 num개 거래를 보여주기 위한 함수 """

    if typeCheck(num, "int") == False :
        win32api.MessageBox(0, f'데이터 타입을 정확하게 입력해주세요.', '알림창')
        return
    
    length = getDataLength()
    if length == 0:
        win32api.MessageBox(0, '저장된 데이터가 없습니다.', '알림창')
        return
    
    if num > length:
        num = length
        #if num is bigger than length, change num into length
    wanted = length - num
    showData = retrieveArrData(length - 1)
    for i in range(length -1, wanted - 1, - 1):
        showData = showData + retrieveArrData(i)
        #retrieveArrData에서 한개씩 받아오면서 여기서 처리하던가 아니면 리턴 받은 모든 데이터를 처리하던가 
        #결정은 당신의 몫이오
    return showData


# In[11]:


#예제 데이터 저장과 최근 거래 내역 조회
_id = "grace"
coin = "eth"
coinNum ="3"
value = 1500
isBought = False
date = "2019.12.1.12시.1분"
storeData(_id, coin, coinNum,value, isBought,date)

(_coin, _coinNum, _date, _isBought, _value) = retrieveMyData_recent(_id)
print(_coin, _coinNum, _date, _isBought, _value )


# In[12]:


#예제 전체 블록 데이터 조회
showData = showDataArr(5)
print(showData)
#예제 아이디로 블록 데이터 조회
showMyData = showDataArr_Id("grace", 10)
print(showMyData)

