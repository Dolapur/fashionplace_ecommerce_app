
let btns = document.getElementsByClassName('addtocart')
for(let i = 0; i < btns.length; i++){
  btns[i].addEventListener('click', function(e){
    let product_id = e.target.dataset.product
    let action = e.target.dataset.action
    console.log(product_id)
    if(user=='AnonymousUser'){
      console.log('Sign in')
    }

    else{
      addToCart(product_id, action)
    }
  })
}

function addToCart(p_id, act){
    const data = {product_id: p_id, action: act};

    let url = '/update_cart'
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      document.getElementById('cart').innerHTML = `<h4>${data.quantity}</h4>`
    })
    .catch((error) => {
      console.error('Error:', error);
    });
    
    }
    
    let inputfields = document.getElementsByTagName('input')
    for(let i =0; i<inputfields.length; i++){
      inputfields[i].addEventListener('change', updateQuantity)
      
    }
    
    function updateQuantity(e){
      let inputvalue = e.target.value
      let product_id = e.target.dataset.product
    
      const data = {p_id: product_id, in_val: inputvalue};
    let url = '/update_quantity'
    
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        e.target.parentElement.parentElement.children[4].innerHTML = `<h3>$${data.get_total.toFixed(2)}</h3>`
        document.getElementById('total').innerHTML = `<h3><strong>$${data.get_cart_total.toFixed(2)}</strong></h3> `
        document.getElementById('cart').innerHTML = `<h4>${data.quantity}</h4>`
        
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
