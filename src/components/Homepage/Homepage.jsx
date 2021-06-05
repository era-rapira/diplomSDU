import React, { useState, useEffect } from 'react';
import { commerce } from '../../lib/commerce';
import Products from '../Products/Products'
import banner1 from '../../assets/banner1.jpg';
import banner2 from '../../assets/banner2.jpg';
import banner3 from '../../assets/banner3.jpg';
import {Carousel} from '3d-react-carousal';
import './index.css';
import { CircularProgress, fade, Grid, withStyles } from '@material-ui/core';
import Product from '../Products/Product/Product';
import ItemsCarousel from 'react-items-carousel';
import SearchIcon from '@material-ui/icons/Search';
import InputBase from '@material-ui/core/InputBase';
import Footer from '../Footer/Footer';

const styles = theme => ({
    root: {
      width: '100%',
    },
    grow: {
      flexGrow: 1,
    },
    menuButton: {
      marginLeft: -12,
      marginRight: 20,
    },
    title: {
      display: 'none',
      [theme.breakpoints.up('sm')]: {
        display: 'block',
      },
    },
    search: {
      position: 'relative',
      borderRadius: theme.shape.borderRadius,
      backgroundColor: fade(theme.palette.common.white, 0.15),
      '&:hover': {
        backgroundColor: fade(theme.palette.common.white, 0.25),
      },
      marginLeft: 0,
      width: '100%',
      [theme.breakpoints.up('sm')]: {
        marginLeft: theme.spacing.unit,
        width: 'auto',
      },
    },
    searchIcon: {
      width: theme.spacing.unit * 9,
      height: '100%',
      position: 'absolute',
      pointerEvents: 'none',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
    },
    inputRoot: {
      color: 'inherit',
      width: '100%',
    },
    inputInput: {
      paddingTop: theme.spacing.unit,
      paddingRight: theme.spacing.unit,
      paddingBottom: theme.spacing.unit,
      paddingLeft: theme.spacing.unit * 10,
      transition: theme.transitions.create('width'),
      width: '100%',
      [theme.breakpoints.up('sm')]: {
        width: 120,
        '&:focus': {
          width: 200,
        },
      },
    },
  });

function Homepage(props) {
    const { classes, cart, setCart, handleAddToCart } = props;
    const [products, setProducts] = useState([]);
    const [filteredProducts, setFilteredProducts] = useState([]);
    const [order, setOrder] = useState({});
    const [errorMessage, setErrorMessage] = useState('');
    const [activeItemIndex, setActiveItemIndex] = useState(0);


    const changeActiveItem = (activeItemIndex) => setActiveItemIndex(activeItemIndex);
    const fetchProducts = async () => {
        const { data } = await commerce.products.list();

        setProducts(data);
    }

    const fetchProductsByQuery = async (query) => {
        if (query.length == 0) {
          setFilteredProducts([]);
        } else {
          const { data } = await commerce.products.list({
            query: `${query}`
        });

        setFilteredProducts(data ?? []);
        }
    }

    const fetchCart = async () => {
        setCart(await commerce.cart.retrieve())
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
            <div className="homepage__filter">
            <div className={classes.search}>
            <div className={classes.searchIcon}>
              <SearchIcon />
            </div>
            <InputBase
              onChange={(event) => {
                  console.log(event.target.value);
                  fetchProductsByQuery(event.target.value)
              }}
              placeholder="Search…"
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
            />
          </div>
            </div>
            <Products products={filteredProducts.length > 0 ? filteredProducts : products} onAddToCart={handleAddToCart} />
            <div className="carousel__products">
            <ItemsCarousel
                // Placeholder configurations
                enablePlaceholder
                numberOfPlaceholderItems={5}
                minimumPlaceholderTime={1000}
                placeholderItem={<CircularProgress></CircularProgress>}

                // Carousel configurations
                numberOfCards={4}
                gutter={12}
                showSlither={true}
                firstAndLastGutter={true}
                freeScrolling={true}

                // Active item configurations
                requestToChangeActive={changeActiveItem}
                activeItemIndex={activeItemIndex}
                activePosition={'center'}

                chevronWidth={24}
                rightChevron={<button style={{ width: '50px', position: 'absolute', backgroundColor: 'aqua'}}>{'>'}</button>}
                leftChevron={<button style={{ width: '50px', position: 'absolute' , backgroundColor: 'aqua'}}>{'<'}</button>}
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
            <Footer/>
        </div>
    )
}
  
  export default withStyles(styles)(Homepage);
