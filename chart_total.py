import json

''' Convert json data into a python object '''
# Create a class from the json data
class SpotifyCharts:
    def __init__(self, rank, uri, artist_names, track_name, source, peak_rank,
        previous_rank, weeks_on_chart, streams):
        self.rank = rank
        self.uri = uri
        self.artist_names = artist_names
        self.track_name = track_name
        self.source = source
        self.peak_rank = peak_rank
        self.previous_rank = previous_rank
        self.weeks_on_chart = weeks_on_chart
        self.streams = streams
    
    # Using a class method
    @classmethod
    def from_json(cls, global_weekly):
        data = json.loads(global_weekly)
        return cls(**data)

    # Calling the specific value we want
    def __repr__(self):
        return f'<SpotifyCharts { self.artist_names }>'

global_weekly = '''{
        "rank": "1",
        "uri": "spotify:track:0V3wPSX9ygBnCm8psDIegu",
        "artist_names": "Taylor Swift",
        "track_name": "Anti-Hero",
        "source": "Taylor Swift",
        "peak_rank": "1",
        "previous_rank": "1",
        "weeks_on_chart": "3",
        "streams": "50080850"
    }'''


''' Extraxt the information the user wants from the data '''
def read_data(path):
    with open(path, "r") as spotify_charts:
        charts_list = list()
        data = json.loads(spotify_charts.read()) # Read the json file
        # Add the aguments from the list in the SpotifyCharts class
        for d in data:
            charts_list.append(SpotifyCharts(**d))
    return charts_list

# Output the info accorfing to user's input
def main():
    list_of_obj = read_data("global_weekly.json")
    print('')
    print('Welcome!')
    print('')
    while True:
        artist_input = input("Give me an Artist Name, in the form of name and last nmame, e.g. Taylor Swift:")
        
        # Fetching the sum of streams from the artist
        sum_of_streams=0
        for obj in list_of_obj:
            if (obj.artist_names).lower() == artist_input.lower(): # Make input case insensitive
                sum_of_streams += int(obj.streams)

        if sum_of_streams !=0:
            # Output the artist name and sum of their streams
            print('')
            print(f'Artist Name: {artist_input}, Streams: {sum_of_streams}')
            print('')
            quit_script = input('Do you want to quit? Answer with y or n :')
            if quit_script.lower() == 'y' or quit_script.lower() == 'yes':
                print('')
                print('Goodbye!')
                break
            if quit_script != 'y' or quit_script != 'yes':
              continue

        # Print message if user typed the name wrong or the artist does not exist
        print('Ooopsss! The name provided is either wrong, or the artist does not exist!')
        cont_or_break = input('Do you want to try again? Answer with y or n :')
        if cont_or_break.lower() == 'n' or cont_or_break.lower() == 'no':
            print('')   
            print('Goodbye!')
            break

        
main()

