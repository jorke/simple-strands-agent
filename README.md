
python simple_agent.py '{"prompt": "What is the weather now?"}'

agentcore configure -e simple_agent.py

agentcore invoke '{"prompt": "What is the weather now?"}'

```
aws bedrock-agentcore tag-resource \
    --resource-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:agent-runtime/example-runtime \
    --tags Key=Environment,Value=Production Key=Team,Value=AI


    ```