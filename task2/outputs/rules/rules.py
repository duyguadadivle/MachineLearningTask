def findDecision(obj): #obj[0]: Outlook, obj[1]: Temperature, obj[2]: Humidity, obj[3]: Windy
	# {"feature": "Outlook", "instances": 14, "metric_value": 0.9403, "depth": 1}
	if obj[0] == 'sunny':
		# {"feature": "Humidity", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[2] == 'high':
			return 'no'
		elif obj[2] == 'normal':
			return 'yes'
		else: return 'yes'
	elif obj[0] == 'rainy':
		# {"feature": "Windy", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[3]<=False:
			return 'yes'
		elif obj[3]>False:
			return 'no'
		else: return 'no'
	elif obj[0] == 'overcast':
		return 'yes'
	else: return 'yes'
