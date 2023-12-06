function convertUsdToBtc() {
    var usdAmount = document.getElementById('usdInput').value;
    fetch(`/convert-usd-to-btc/?usd_price=${usdAmount}`)
        .then(response => response.json())
        .then(data => {
            const formattedUsd = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(data.usd_price);
            const formattedBtc = new Intl.NumberFormat('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 8 }).format(data.bitcoin_price);
            document.getElementById('result').innerText = `USD: ${formattedUsd} / BTC: ${formattedBtc}`;
        })
        .catch(error => console.error('Error:', error));
}

function convertBtcToUsd() {
    var btcAmount = document.getElementById('btcInput').value;
    fetch(`/convert-btc-to-usd/?btc_amount=${btcAmount}`)
        .then(response => response.json())
        .then(data => {
            const formattedBtc = new Intl.NumberFormat('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 8 }).format(data.btc_amount);
            const formattedUsd = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(data.usd_price);
            document.getElementById('result').innerText = `BTC: ${formattedBtc} / USD: ${formattedUsd}`;
        })
        .catch(error => console.error('Error:', error));
}
