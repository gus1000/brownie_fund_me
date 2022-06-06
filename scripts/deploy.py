

from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def deploy_fund_me():
    account = get_account()
    
    #pass the price feed address to our fundme contract
    #if we are on a persistent network like runkeby, use the associated address
    #otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS: #pull address from the network config...ganache local  isnt development
        price_feed_address = config["networks"][network.show_active()]
        ["eth_usd_price_feed"]
    else:
       deploy_mocks()
       price_feed_address = MockV3Aggregator[-1].address  #we created a mock price feed
        
    
    
    fund_me = FundMe.deploy(price_feed_address, {"from" : account}, publish_source= config["networks"]
    [network.show_active()].get("verify"), ) # <--- this is a state change
    
    
    
    print(f"contract deployed to {fund_me.address}")
    return fund_me
    
#port must be 8545 ...reset ganache 
def main():
    deploy_fund_me() #you have to reset ganache settings from prot 7545 to port 8545...change host name
#leave ganache open or else all contracts will be lost ...you will be unable to interact with them again 