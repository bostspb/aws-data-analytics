import boto3
from boto3.dynamodb.conditions import Attr, Key
from tabulate import tabulate
import time

TABLE_NAME = 'player_score'
SECONDS_TO_MILIS = 1000
MAX_RECORDS_TO_PRINT = 10


def print_player_data(all_items, total_duration, total_consumed_capacity):
    total_records = len(all_items)
    formated_records = convert_player_data_to_array(all_items)
    print(tabulate(formated_records,
                   headers=['Name', 'Game', 'Score', 'Timestamp', 'Badges'],
                   tablefmt='pretty'))
    print('Printed {} of {} records returned'.format(len(formated_records),
                                                     total_records))
    print('Consumed Capacity: {}'.format(total_consumed_capacity))
    print('Duration: {} miliseconds'.format(total_duration))


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
    total_consumed_capacity = 0
    all_items = list()

    player_game_data = score_table.scan(
        FilterExpression=Attr('badge').eq('Champs'),
        ReturnConsumedCapacity='TOTAL')
    total_consumed_capacity = player_game_data['ConsumedCapacity'] \
        ['CapacityUnits']
    all_items.extend(player_game_data['Items'])


    # If the result of the first batch is not complete. Pagination is required
    while 'LastEvaluatedKey' in player_game_data:
        player_game_data = score_table.scan(
            FilterExpression=Attr('badge').eq('Champs'),
            ExclusiveStartKey=player_game_data['LastEvaluatedKey'],
            ReturnConsumedCapacity='TOTAL')
        total_consumed_capacity = total_consumed_capacity + \
                                  player_game_data['ConsumedCapacity'][
                                      'CapacityUnits']
        all_items.extend(player_game_data['Items'])


    end_time = time.time()
    duration = int((end_time - start_time) * SECONDS_TO_MILIS)

    print_player_data(all_items, duration, total_consumed_capacity)
