import boto3
from boto3.dynamodb.conditions import Attr, Key
from tabulate import tabulate
import time

TABLE_NAME = 'player_score'
SECONDS_TO_MILIS = 1000
MAX_RECORDS_TO_PRINT = 5

def print_player_data(dynamo_result, total_duration=None):
    items_to_print = dynamo_result['Items']
    total_records = len(items_to_print)
    formated_records = convert_player_data_to_array(items_to_print)
    print(tabulate(formated_records,
                   headers=['Name', 'Game', 'Score', 'Timestamp', 'Badges'],
                   tablefmt='pretty'))
    print('Printed {} of {} records returned'.format(len(formated_records), total_records))
    print_capacity(dynamo_result)
    print('Duration: ' + str(total_duration) + ' miliseconds')

def print_capacity(get_item_result):
    print('Consumed Capacity: '
          + str(get_item_result['ConsumedCapacity']['CapacityUnits']))


def convert_player_data_to_array(items_to_print):
    current_position = 0
    array_to_print = []
    while current_position < len(items_to_print) \
        and current_position < MAX_RECORDS_TO_PRINT:
        item_array = [items_to_print[current_position]['player_name'],
                      items_to_print[current_position]['game'],
                      items_to_print[current_position]['score'],
                      items_to_print[current_position]['game_timestamp']]
        if 'badge' in items_to_print[current_position]:
            item_array.append(items_to_print[current_position]['badge'])
        else:
            item_array.append("")
        array_to_print.append(item_array)
        current_position = current_position + 1
    return array_to_print


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb')
    score_table = dynamodb.Table(TABLE_NAME)

    start_time = time.time()
    player_game_data = score_table.query(
        KeyConditionExpression=Key('player_name').eq('James Smith'),
        # Follow lab step to uncomment the following statements.
        # FilterExpression=Attr('badge').eq('Champs'),
        # Limit=5,
        ReturnConsumedCapacity='TOTAL')

    end_time = time.time()

    duration = int((end_time - start_time) * SECONDS_TO_MILIS)
    print_player_data(player_game_data, duration)
