import React from 'react';
import { Typography, Button, Card, CardActions, CardContent, CardMedia} from '@material-ui/core';

import './index.css'
import useStyles from './styles'

const CartItem = ({ item, onUpdateCartQty, onRemoveFromCart }) => {
    const classes = useStyles();

    return (
        <Card className="cart__card" >
            <CardMedia className="cart__card__media" image={item.media.source} alt={item.name}  />
            <CardContent className="cart__card__content">
                <Typography variant="h4">{item.name}</Typography>
                <Typography variant="h5">{item.line_total.formatted_with_symbol}</Typography>
            </CardContent>
            <CardActions className="cart__card__actions">
                <div className={classes.buttons}>
                    <Button type="button" size="small" onClick={() => onUpdateCartQty(item.id, item.quantity - 1)}>-</Button>
                    <Typography>{item.quantity}</Typography>
                    <Button type="button" size="small" onClick={() => onUpdateCartQty(item.id, item.quantity + 1)}>+</Button>
                </div>
                <Button variant="contained" type="button" color="secondary" onClick={() => onRemoveFromCart(item.id)}>Remove</Button>
            </CardActions>

        </Card>
    )
}

export default CartItem
