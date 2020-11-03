Portfolio Optimization for Retail Investors
==============================

While ETFs do provide low-cost access to a variety of asset classes, industry sectors, and international markets, they do carry some unique risks.  For e.g. trading fees and lack of liquidity. We shall explore  research-backed techniques of portfolio diversification as possible alternatives to ETF-investing.

In this notebook, several portfolio optimization techniques are used  to find the best portfolio-allocation strategy. The objective is to **employ well-documented portfolio-optimization methods as a retail investor.**

---

As a long-term retail investor myself, I truly believe in high-growth and innovative companies. This is a pet project aimed for my own interests in investing. My content is focused on the following:

- Apply a variety of portfolio-optimization techniques
- Back-test optimized portfolio-allocation weights on out-of-sample data.

*I am long in the positions stated in my analysis. I am not receiving compensation for it. I have no business relationship with any company whose stock is mentioned in this analysis.*



## Set up

Requirements:

- Git
- Docker
- Python3

Development environment and dependencies are maintained using docker.  Use the following code to start a docker container required for development.

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

Using the above Portfolio Optimization Techniques, 3 configurations of portfolio weights are hand-picked:

1. `EFO w/ 'Max Sharpe'`
2. `EFO w/ 'Min Volatility w/ L2'`
3. `'100% TSLA'`



#### Background

- In notebook `investing_opt/notebooks/pyportfolioopt_011120.ipynb`, the subject assets are **TSLA**, **ARKK** and **AAPL**.  
- Back-testing was done on out-of-sample data, and commission fees (@0.08% according to Saxo Broker) was also accounted for.
  - 2015-01-01 to 2019-12-31 for *optimization*
  - 2020-01-01 to 2020-11-01 (YTD) for *backtesting*

---

![absolute returns chart](https://github.com/longwind48/investing-opt/blob/main/investing_opt/reports/figures/ytd_portfolio_perf_efo_min_vol_l2_011120.png)

**Observations** (backtested on *adjusted* closing prices):

- With an initial investment sum of $100,000, EFO-optimized portfolio will yield 154.33% returns YTD.
- Whereas the market, SPY, will only yield 1.96% in returns YTD.
- Absolute returns have already accounted for 0.08% commission fees, and are based off adjusted closing prices. 

---

**Observations** (backtested on non-adjusted closing prices):

- `'EFO w/ Max Sharpe'` attained the lowest PNL @ 59.18%
- `'EFO w/ Min Volatility w/ L2'` attained a significantly improved PNL @ 151.91%
- `'100% TSLA'` attained a jaw-dropping PNL @ 347.09%
- Markowitz’s method of optimization `'EFO w/ Max Sharpe'` assigned a weight of zero to TSLA. This is expected because this method is known to set many of the asset weights to be zero. A workaround is to introduce L2 regularization to the objective function, which is what we did to `'EFO w/ Min Volatility w/ L2'`.
- We can speculate that TSLA's zero allocation is due of its high correlation with ARKK. (Afterall, ARKK has TSLA as the top holding, as of 01 Nov 2020)
- `'100% TSLA' strategy'` yielded a max drawdown of 60.6% YTD and a max drawdown period of 75 days. Some might vehemently disagree with this strategy as it defies all logic that points to diversification. As a firm believer of Tesla, this is still a strategy worth evaluating.

 

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



Assuming one start with an initial portfolio value of $100,000, he/she would have yielded 151.91% in capital gains over a span of 305 days. If we compare to the market, the S&P500 would have yielded 1.21% YTD. 

#### Final Thoughts

There is no sound way to evaluate the value of a EFO-optimized portfolio. This is because, in the real world, there are many factors that affect allocation weights. For example, the investor could be fired up after reading up on company X's news, and decided to increase his/her position size for that stock. Or perhaps he/she has extra cashflow for the month, and felt like investing more. Position sizes could also be increased for some company if it is due for a big event, or if it is oversold. 

I could set on some baseline measure for comparison, for example, equal weights for all assets in portfolio. However, I decided against it because this is an uncommon sight in real-world investing. 

Afterall, this is a project designed to benefit any retail investor. I think that comparing the portfolio with the market index is the most appropriate measure. 

**Personally, these observations further re-affirmed my long position in innovative companies like Tesla. Innovative and disruptive companies do outperform in the midst of a crisis.** 

## Further Work

Stay tuned for more:

- [ ] Evaluate different different configs for portfolio weights on periodic investments
- [x] Use Adjusted Closing prices
- [ ] Project annual returns using machine learning
- [ ] Deploy 'Portfolio-Optimization + Backtesting' as a service using the following setup:
  - FastAPI as web framework
  - Gunicorn as WSGI application server
  - Nginx as web server, if there is static content.
- [ ] Configure Travis CI for CI pipelines



## Resources

Immensely grateful to the following sources:

- https://pyportfolioopt.readthedocs.io/en/latest/index.html

- https://enzoampil.github.io/fastquant-blog/

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>