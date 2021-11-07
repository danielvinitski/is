// const url = process.env.CUSTOMER_API_URL;

$(document).ready(function () {
    $("#price").keyup(function(event){
        if( $('#price').val() && $('#customerId').val() && $('#customerName').val()) {
            $( "#buyButton" ).prop('disabled', false);
        }else{
            $( "#buyButton" ).prop('disabled', true);
        }
    });
    $("#customerName").keyup(function(event){
        if( $('#price').val() && $('#customerId').val() && $('#customerName').val()) {
            $( "#buyButton" ).prop('disabled', false);
        }else{
            $( "#buyButton" ).prop('disabled', true);
        }
    });
    $("#customerId").keyup(function(event){
        if( $('#price').val() && $('#customerId').val() && $('#customerName').val()) {
            $( "#buyButton" ).prop('disabled', false);
        }else{
            $( "#buyButton" ).prop('disabled', true);
        }
    });
    $( "#buyButton" ).click(function(event) {
        event.preventDefault();
        let price = $('#price').val();
        let customerId = $('#customerId').val();
        let customerName = $('#customerName').val();
        let headers = {
            // "Access-Control-Request-Headers": "Content-Type",
            // "Access-Control-Allow-Origin": "*",
            // "Access-Control-Allow-Methods": "POST",
            "Content-Type": "application/json"
        };
        let data = {
            price: price,
            username: customerName,
            userId: customerId
        };
        $.ajax({
            url: url + "/api/v1/buy",
            type: 'POST',
            headers: headers,
            data: JSON.stringify(data),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            async: false
        }) ;
        $('#price').val("");
        $('#customerId').val("");
        $('#customerName').val("");
    });

    $( "#getAllBuy" ).click(function() {
        $.ajax({
            url: url + "/api/v1/getBuyList",
            type: 'GET',
            contentType: 'application/json; charset=utf-8',
            async: false
        }).done(function(data) {
            $( "#card" ).text(data);
        }).fail(function() {
            alert( "error" );
        });
    });
});
