# Usage

To use YDR in a project:

```
import ydr
```

# read historical bank nifty data
nb = ydr.get_data("banknifty_index")

# initiate strategy class
st = ydr.strategy()

st.add_indicator("MV,period=5")

st.buy()
st.sell()
