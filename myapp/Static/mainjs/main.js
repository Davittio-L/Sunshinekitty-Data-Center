function convertUsdToBtc() {
    var usdAmount = document.getElementById('usdInput').value;
    fetch(`/convert-usd-to-btc/?usd_price=${usdAmount}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = 
                `USD: ${data.usd_price} / BTC: ${data.bitcoin_price}`;
        })
        .catch(error => console.error('Error:', error));
}

function convertBtcToUsd() {
    var btcAmount = document.getElementById('btcInput').value;
    fetch(`/convert-btc-to-usd/?btc_amount=${btcAmount}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = 
                `BTC: ${data.btc_amount} / USD: ${data.usd_price}`;
        })
        .catch(error => console.error('Error:', error));
}