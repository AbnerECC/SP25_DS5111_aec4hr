import sys
sys.path.append('/home/ubuntu/SP25_DS5111_aec4hr/bin/gainers/')
from base import GainerFactory, ProcessGainer


if __name__=="__main__":
   
    # Make our selection, 'one' choice
    choice = sys.argv[1]

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()