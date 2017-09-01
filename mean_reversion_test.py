def initialize(context):
    context.aapl =sid(24)
    
    schedule_function(test_order,date_rules.every_day(),time_rules.market_close(minutes=30))


def before_trading_start(context,data):
    hist = data.history(context.aapl, 'price', 30, '1d')
    prices_10 = hist[-5:]
    prices_30 = hist
    context.sma_10 = prices_10.mean()
    context.sma_30 = prices_30.mean()

def test_order(context,data):
    
    if context.sma_10<context.sma_30 and context.portfolio.positions[context.aapl].amount==0 :
        order_percent(context.aapl,1.0)
    if context.sma_10>context.sma_30 and context.portfolio.positions[context.aapl].amount>0 :
        order(context.aapl, -1*context.portfolio.positions[context.aapl].amount)
	
