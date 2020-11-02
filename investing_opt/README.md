Portfolio Optimization for Retail Investors
==============================

While ETFs do provide low-cost access to a variety of asset classes, industry sectors, and international markets, they do carry some unique risks.  For e.g. trading fees and lack of liquidity. We shall explore  research-backed techniques of portfolio diversification as an possible  alternative to ETF-investing.

In this notebook, several portfolio optimization techniques are used  to find the best portfolio-allocation strategy. The objective is to **employ well-documented portfolio-optimization methods as a retail investor.**

---

As a retail investor myself, I truly believe in high-growth and innovative companies. This is a pet project aimed for my own interests in investing. My content focus on the following:

- Apply a variety of portfolio-optimization techniques
- Back-test optimized portfolio-allocation weights on out-of-sample data.

*I am long in the positions stated in my analysis. I am not receiving compensation for it. I have no business relationship with any company whose stock is mentioned in this analysis.*



## Set up

Development environment and dependencies are maintained using docker.  

```shell
$ git clone https://github.com/longwind48/investing-opt.git
$ cd investing-opt

# Automate docker build and run using script
$ python3 run_docker.py

# Get jupyter notebook token
$ docker logs investing_opt_dev

# Visit localhost:9999 and input token to access jupyter notebook

```



## Portfolio Optimization Techniques

- [x] Efficient Frontier Optimisation (EFO), with the following objective functions:
  - [x] Maximum Sharpe ratio
  - [x] Minimum volatility
  - [x] Efficient return
  - [x] Efficient risk
- [x] Critical Line Algorithm (CLA), with the following objective functions:
  - [x] Maximum Sharpe ratio
  - [x] Minimum volatility
- [ ] Particle Swarm Optimization



## Analysis

**Notes:**

- When backtesting, we used:
  - 2015-01-01 to 2019-12-31 for *optimization*
  - 2020-01-01 to 2020-11-01 (YTD) for *backtesting*
- `get_stock_data()` function retrieves the daily closing prices from yahoo finance. Adjusted closing prices are more appropriate because they account for cash and stock dividends.

---

There are 3 configurations of portfolio weights:

1. `EFO w/ 'Max Sharpe'`
2. `EFO w/ 'Min Volatility w/ L2'`
3. `'100% TSLA'`



**Observations:**

- `'EFO w/ Max Sharpe'` attained the lowest PNL @ 59.18%
- `'EFO w/ Min Volatility w/ L2'` attained a significantly improved PNL @ 151.91%
- `'100% TSLA'` attained a jaw-dropping PNL @ 347.09%
- Markowitz’s method of optimization `'EFO w/ Max Sharpe'` assigned a weight of zero to TSLA. This is expected because this method is known to set many of the asset weights to be zero. A workaround is to introduce L2 regularization to the objective function, which is what we did to `'EFO w/ Min Volatility w/ L2'`.
- We can speculate that TSLA's zero allocation is due of its high correlation with ARKK. (Afterall, ARKK has TSLA as the top holding, as of 01 Nov 2020)
- `'100% TSLA' strategy'` yielded a max drawdown of 60.6% YTD and a max drawdown period of 75 days. Some might violently disagree with this strategy as it defies all logic that points to diversification. To my defence, this is still a strategy worth evaluating.

 

```
# 'Min Volatility w/ L2' Config

Initial Portfolio Value @ 2020-01-01: $100000
Current Portfolio Value @ 2020-11-01: $251914
Investment Horizon: 305 days
Portfolio Allocation and Initial Cash : {
    "TSLA_adj_close": {
        "weight": 0.3174899792368109,
        "init_cash": 31748.997923681087
    },
    "ARKK_adj_close": {
        "weight": 0.3401246003872266,
        "init_cash": 34012.46003872266
    },
    "AAPL_adj_close": {
        "weight": 0.3423854203759626,
        "init_cash": 34238.54203759626
    }
}
Profit and Loss (percent): 151.91%
```



## Further Work

- [ ] Evaluate different different configs for portfolio weights on periodic investments
- [ ] Use Adjusted Closing prices
- [ ] Deploy 'Portfolio-Optimization + Backtesting' as a service using the following setup:
  - FastAPI as web application
  - Gunicorn as WSGI application server
  - Nginx as web server, if there is static content.
- [ ] Configure Travis CI for CI pipelines



## Resources

Immensely grateful to the following sources:

- https://pyportfolioopt.readthedocs.io/en/latest/index.html

- https://enzoampil.github.io/fastquant-blog/

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>