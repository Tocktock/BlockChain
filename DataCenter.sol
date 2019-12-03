pragma solidity >=0.4.22 <0.6.0;

contract DataCenter {
    
    struct Data {
        string id;
        string coin;
        string coinNum;
        string date;
        bool isBought; 
        uint value;
    }
    
    struct MyData {
        Data[] myData;
    }
    
    mapping (string => MyData) data_list;
    Data[] dataArr;
    
    function storeData(string memory key, string memory coin, string memory coinNum, uint value,bool isBought, string memory date) public returns (bool)
    { //function for store the data
        
        Data memory temp;
        temp.coin = coin;
        temp.id = key;
        temp.coinNum=coinNum;
        temp.date = date;
        temp.isBought = isBought;
        temp.value = value;
        
        data_list[key].myData.push(temp);
        dataArr.push(temp);
        return true;
    }
    
    function retrieveMyData_recent(string memory key) public view returns (string memory,string memory, string memory, bool, uint )  // function for RetrieveCoinData
    {
        uint index = data_list[key].myData.length - 1; 
        
        return (data_list[key].myData[index].coin, data_list[key].myData[index].coinNum, data_list[key].myData[index].date, data_list[key].myData[index].isBought,
        data_list[key].myData[index].value);
    }
    
    
    function retrieveMyData_index (string memory key, uint index) public view returns (string memory,string memory, string memory, bool, uint )  // function for RetrieveCoinData
    {
        require(index < data_list[key].myData.length);
        
        return (data_list[key].myData[index].coin, data_list[key].myData[index].coinNum, data_list[key].myData[index].date, data_list[key].myData[index].isBought,
        data_list[key].myData[index].value);
    }
    
    function retrieveArrData(uint index) public view returns (string memory,string memory,string memory, string memory, bool, uint )
    {
        return (dataArr[index].id, dataArr[index].coin, dataArr[index].coinNum, dataArr[index].date ,dataArr[index].isBought,dataArr[index].value );
    }
    
    function getMyDataLength(string memory key) public view returns (uint ) { //function for GetDataLength
        return data_list[key].myData.length;
    }
    
    function getDataLength() public view returns (uint ) { //function for GetDataLength
        return dataArr.length;
    }

}