# InlineResponse2001CurrentParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_fee** | **float** | Bank fees accounting at conversion | [optional] [default to 0.007]
**default_market_update_rate** | **int** | Default market&#39;s depth update rate in seconds | [optional] [default to 20]
**fiat_update_delay** | **int** | Delay in seconds between an exchange rate updates | [optional] 
**market_expiration_time** | **int** | Markets order book expiration time | [optional] 
**markets** | **list[str]** | List of market names | [optional] 
**max_tx_volume** | **float** | The max money volume that can be involved into transfer | [optional] [default to 10.0]
**observers** | **list[str]** | List of opportunity observers names | [optional] 
**refresh_rate** | **int** | Update rate in seconds of the arbiter&#39;s main loop | [optional] [default to 20]
**report_queue** | **str** | The name of the response queue | [optional] [default to 'arbitrage_watcher']
**amqp_url** | **str** | Connection url to the amqp broker | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


