import { Card, CardContent, CardMedia, CircularProgress, CardActions, Typography, IconButton  } from '@material-ui/core';
import React, { useEffect, useState } from 'react'
import { AddShoppingCart } from '@material-ui/icons';
import { useParams } from 'react-router';
import { commerce } from '../../lib/commerce';

function ProductPage({ onAddToCart }) {
    
    const [product, setProduct] = useState(null);
    let { productId } = useParams();


    useEffect(() => {
        handleFetchProduct()
    }, [])

    const handleFetchProduct = () => {
        commerce.products.retrieve(productId)
  .then((product) => setProduct(product));
    }

    return (
        product ? <Card className="product__card" >
        <CardMedia className="product__card__media" image={product.media.source} title={product.name} />
        <CardContent>
            <div className="product__card__content">
                <Typography variant='h5' gutterBottom>
                    {product.name}
                </Typography>
                <Typography variant='h5'>
                    {product.price.formatted_with_symbol}
                </Typography>
            </div>
            <Typography dangerouslySetInnerHTML={{ __html: product.description}} variant="body2" color="textSecondary" />
        </CardContent>
        <CardActions disableSpacing className="product__card__actions">
            <IconButton aria-label="Add to Cart" onClick={() => onAddToCart(product.id, 1)}>
                <AddShoppingCart />
            </IconButton>
        </CardActions>
    </Card> : <CircularProgress/>
    )
}

export default ProductPage
