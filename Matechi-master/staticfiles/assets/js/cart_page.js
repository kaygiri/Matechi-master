var update_btn = document.getElementById('update-cart-btn');
update_btn.addEventListener('click', function(e){
    var input_values = document.getElementsByClassName('input-spinner-form')
    console.log(input_values)
    
    for (i = 0; i<input_values.length; i++)
    {
        if (i%2 == 0)
        {
            if (user == 'AnonymousUser')
            {
                console.log('Not logged in');
            }
            else{
                quantity = (input_values[i].value);
                product_id = (input_values[i].dataset.product);
                action = 'update'
                update_cart(quantity, product_id, action);
            }
        }
    }
})

update_cart = (quantity, productId, action)=>{
    console.log('User authenticated ... Sending data');

    var url = '/update-cart/'

    fetch(url, {
        method : 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({'productId' : productId, 'action' : action, 'quantity' : quantity})
    })

    .then((response)=>{
        console.log(response);
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}


// When remove button placed, delete the product in the cart

var del_btn = document.getElementsByClassName('btn-remove');
for (i=0; i<del_btn.length; i++)
{
    del_btn[i].addEventListener('click', function(e) {
        quantity = 0;
        product_id = (this.dataset.product);
        action = 'delete'
        update_cart(quantity, product_id, action);
    })
}