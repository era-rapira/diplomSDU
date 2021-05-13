import React, { useState, useEffect } from 'react';
import { commerce } from '../../lib/commerce';
import Products from '../Products/Products'
import banner1 from '../../assets/banner1.jpg';
import banner2 from '../../assets/banner2.jpg';
import banner3 from '../../assets/banner3.jpg';
import {Carousel} from '3d-react-carousal';
import './index.css';
import { Grid } from '@material-ui/core';
import Product from '../Products/Product/Product';
import ItemsCarousel from 'react-items-carousel';

function Homepage() {
    const [products, setProducts] = useState([]);
    const [cart, setCart] = useState({});
    const [order, setOrder] = useState({});
    const [errorMessage, setErrorMessage] = useState('');
    const [activeItemIndex, setActiveItemIndex] = useState(0);


    const changeActiveItem = (activeItemIndex) => setActiveItemIndex(activeItemIndex);
    const fetchProducts = async () => {
        const { data } = await commerce.products.list();

        setProducts(data);
    }

    const fetchCart = async () => {
        setCart(await commerce.cart.retrieve())
    }

    const handleAddToCart = async (productId, quantity) => {
        const { cart } = await commerce.cart.add(productId, quantity);

        setCart(cart);
    }

    const handleUpdateCartQty = async (productId, quantity) => {
        const { cart } = await commerce.cart.update(productId, { quantity });

        setCart(cart);
    }

    const handleRemoveFromCart = async (productId) => {
        const { cart } = await commerce.cart.remove(productId);

        setCart(cart);
    }

    const handleEmptyCart = async () => {
        const { cart } = await commerce.cart.empty();

        setCart(cart);
    }

    const refreshCart = async () => {
        const newCart = await commerce.cart.refresh();

        setCart(newCart);
    }

    const handleCaptureCheckout = async (checkoutTokenId, newOrder) => {
        try {
            const incomingOrder = await commerce.checkout.capture(checkoutTokenId, newOrder);

            setOrder(incomingOrder);
            refreshCart();
        } catch (error) {
            setErrorMessage(error.data.error.message);
        }
    }

    useEffect(() => {
        fetchProducts();
        fetchCart();
    }, []);
    
    let slides = [
        <img  src={banner1} alt="1" />,
        <img  src={banner2} alt="2" />,
        <img  src={banner3} alt="3" />  
    ];

    return (
        <div className="homepage">
            <div style={{ height: '60px'}}/>
            
            <div className="carousel__content">
            <Carousel slides={slides} autoplay={true} interval={5000}/>
            </div>
            <div className="carousel__products">
            <ItemsCarousel
                // Placeholder configurations
                enablePlaceholder
                numberOfPlaceholderItems={5}
                minimumPlaceholderTime={1000}
                placeholderItem={<div style={{ height: 200, background: '#900' }}>Placeholder</div>}

                // Carousel configurations
                numberOfCards={3}
                gutter={12}
                showSlither={true}
                firstAndLastGutter={true}
                freeScrolling={false}

                // Active item configurations
                requestToChangeActive={changeActiveItem}
                activeItemIndex={activeItemIndex}
                activePosition={'center'}

                chevronWidth={24}
                rightChevron={'>'}
                leftChevron={'<'}
                outsideChevron={false}
            >
                {products.map((product) => (
                    <div className="carousel__products__item">
<Grid item key={product.id} xs={12}>
                        <Product product={product} onAddToCart={handleAddToCart} />
                    </Grid> 
                    </div>
                ))}
            </ItemsCarousel>
            </div>
            <Products products={products} onAddToCart={handleAddToCart} />
        </div>
    )
}

export default Homepage
