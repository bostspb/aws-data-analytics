import boto3
from tabulate import tabulate
import time

TABLE_NAME = 'player_score'
SECONDS_TO_MILIS = 1000


def print_player_data(get_item_result):
    player_data = get_item_result['Item']
    print(tabulate([convert_player_data_to_array(player_data)],
                   headers=['Name', 'Game', 'Score', 'Timestamp'],
                   tablefmt='pretty'))
    print('Total Items Returned: 1')


def convert_player_data_to_array(player_data):
    return [player_data['player_name'], player_data['game'],
            player_data['score'], player_data['game_timestamp']]


def print_capacity(get_item_result):
    print('Consumed Capacity: '
          + str(get_item_result['ConsumedCapacity']['CapacityUnits']))


def print_data(dynamo_result, total_duration):
    print_player_data(dynamo_result)
    print_capacity(dynamo_result)
    print('Duration: ' + str(total_duration) + ' miliseconds')


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb')
    score_table = dynamodb.Table(TABLE_NAME)

    start_time = time.time()

    player_game_data = score_table.get_item(
        Key={
            'player_name': 'James Smith',
            'game_timestamp': 1461351017
        },
        ReturnConsumedCapacity='TOTAL')

    end_time = time.time()
    duration = int((end_time - start_time) * SECONDS_TO_MILIS)
    print_data(player_game_data, duration)
