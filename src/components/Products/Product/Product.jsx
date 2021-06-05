import React from 'react';
import { Card, CardMedia, CardContent, CardActions, Typography, IconButton } from '@material-ui/core';
import { AddShoppingCart } from '@material-ui/icons';
import './index.css'

import useStyles from './styles';
import { Link } from 'react-router-dom';

const Product = ({ product, onAddToCart }) => {
    const classes = useStyles();

    return (
        <Card className="product__card" >
            <Link to={`/product/${product.id}`} style={{ textDecoration: 'none'}}>
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
            </Link>
            <CardActions disableSpacing className="product__card__actions">
                <IconButton aria-label="Add to Cart" onClick={() => onAddToCart(product.id, 1)}>
                    <AddShoppingCart />
                </IconButton>
            </CardActions>
        </Card>
    );
}

export default Product
