var addtocartbtn = document.getElementById('add-to-cart-btn');
addtocartbtn.addEventListener('click', function(e){
    var quantity = document.getElementById('qty').value;
    var productId = this.dataset.product;
    var action = this.dataset.action;

    if (user == 'AnonymousUser')
    {
        console.log('User not logged in');
        e.preventDefault();
        _base = window.location.origin;
        window.location.href = _base + '/accounts/login/?next=/cart/';
    }
    else
    {
        updateUserOrder(productId,action,quantity);
    }
})

// When Add to cart pressed update the cart with the item
var updatebtns = document.getElementsByClassName('update-cart');

for (i=0; i<updatebtns.length; i++)
{
    updatebtns[i].addEventListener('click',function(e){
        e.preventDefault();
        var productId = this.dataset.product;
        var action = this.dataset.action;

        console.log(user);
        if (user == 'AnonymousUser')
        {
            console.log('User not logged in');
        }
        else
        {
            updateUserOrder(productId,action);
        }
    })
}

// Update function
updateUserOrder = (productId,action,quantity)=>{
    console.log('User authenticated ... Sending data');

    var url = '/cart/'

    fetch(url, {
        method : 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({'productId' : productId, 'action' : action, 'quantity' : quantity})
    })

    .then((response)=>{
        return (response.json());
    })

    .then((data) => {
        $('#cartModal').modal();
            setTimeout(
                function() {
                    $('#cartModal').modal('hide');
                    location.reload();
                }, 2000);   
    })
}

// When Plus button pressed increase the quantity
plusbtn = document.getElementsByClassName('cart-plus');
console.log(plusbtn);
for (let i=0; i < plusbtn.length; i++) 
{ 
    plusbtn[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        updateUserOrder(productId,action);
    })
}

// When Minus button pressed increase the quantity
minusbtn = document.getElementsByClassName('cart-minus');
console.log(minusbtn);
for (let i=0; i < minusbtn.length; i++) 
{ 
    minusbtn[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        updateUserOrder(productId,action);
    })
}

// When Minus button pressed increase the quantity
removebtn = document.getElementsByClassName('btn-remove');
console.log(removebtn);
for (let i=0; i < removebtn.length; i++) 
{ 
    removebtn[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        updateUserOrder(productId,action);
    })
}

// Take value from input of cart quantity
cart_quantity = document.getElementsByClassName('cart-quantity');
for (let i = 0; i < cart_quantity.length; i++)
{
    cart_quantity[i].addEventListener('change',function(){
        quantity = cart_quantity[i].value;
        productId = this.dataset.product;
        action = this.dataset.action;
        replace_item(quantity,productId,action);
    })
}

var replace_item = (quantity,productId,action)=>{
    var url = '/update_item/'

    fetch(url,{
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFTOKEN' : csrftoken
        },
        body : JSON.stringify({'quantity' : quantity, 'productId' : productId, 'action' : action})
    })

    .then((response)=>{
        return (response);
    })
    
    .then((data)=>{
        location.reload();
    })
}


