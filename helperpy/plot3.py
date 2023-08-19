from functools import partial

import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def process_data(data):
    # convert to dataframe
    df = pd.DataFrame(data, columns=["x", "y"])
    print(df)

    return df

def plot(data):

    sns.set(style="darkgrid")
    plt.figure(figsize=(8, 4.5))
    sns.scatterplot(data=data, x="x", y="y")
    sns.lineplot(data=data, x="x", y="y", markers=False, dashes=True)
    #plt.savefig("plots/all.png")
    plt.show()

if __name__ == "__main__":
    tourneydata = [(33583.3333,57300.0), (33933.3333,56250.0), (33466.6667,55200.0), (33683.3333,54650.0), (33116.6667,54816.6667), (31466.6667,56833.3333), (31516.6667,57583.3333), (31683.3333,57683.3333), (32200.0,58000.0), (33255.8333,58019.1667), (33950.0,57900.0), (34000.0,58250.0), (34153.0556,58176.6667), (33983.3333,58250.0), (32366.6667,57850.0), (32483.3333,57750.0), (32416.6667,57383.3333), (32716.6667,57466.6667), (33583.3333,57583.3333), (33683.3333,57566.6667), (34483.3333,56850.0), (34519.7222,56798.8889), (34283.3333,56916.6667), (33100.0,57733.3333), (32683.3333,57633.3333), (32350.0,57200.0), (32333.3333,57050.0), (31766.6667,56016.6667), (31916.6667,56016.6667), (31900.0,55466.6667), (31883.3333,55433.3333), (31750.0,55466.6667), (32650.0,54450.0), (32516.6667,53483.3333), (33250.0,54016.6667), (33516.6667,54916.6667), (34750.0,55333.3333), (34733.3333,55716.6667), (34833.3333,56233.3333), (34800.0,56216.6667), (32866.6667,56466.6667), (32800.0,56416.6667), (32833.3333,56183.3333), (32600.0,55583.3333), (32833.3333,55483.3333), (33350.0,55633.3333), (33816.6667,55550.0), (33016.6667,56483.3333), (33366.6667,56483.3333), (33333.3333,56933.3333), (33500.0,56866.6667), (33416.6667,57066.6667), (34433.3333,57883.3333), (34466.6667,57850.0), (34400.0,57883.3333), (34416.6667,57733.3333), (34850.0,56216.6667), (34850.0,56233.3333), (34870.5556,56133.6111), (34883.3333,56150.0), (34790.2778,56350.0), (33966.6667,57100.0), (34350.0,57300.0), (34400.0,57333.3333), (34316.6667,56800.0), (34319.1667,56805.2778), (34350.0,56650.0), (32900.0,56133.3333), (32866.6667,55916.6667), (32750.0,55650.0), (32883.3333,55416.6667), (34453.3333,56390.5556), (34383.3333,56766.6667), (34233.3333,56866.6667), (33866.6667,57000.0), (33216.6667,56683.3333), (32033.3333,55666.6667), (32000.0,55483.3333), (31816.6667,55216.6667), (31750.0,55016.6667), (31683.3333,54650.0), (31683.3333,54766.6667), (31316.6667,55200.0), (31433.3333,55233.3333), (31200.0,55750.0), (30250.0,57583.3333), (30716.6667,56600.0), (31800.0,56133.3333), (32916.6667,54966.6667), (32683.3333,54633.3333), (31250.0,55333.3333), (31833.3333,55766.6667), (32616.6667,55833.3333), (33716.6667,54533.3333), (34066.6667,53933.3333), (34400.0,53783.3333), (34366.6667,53766.6667), (33983.3333,53983.3333), (33283.3333,53933.3333), (32700.0,53966.6667), (32033.3333,54183.3333), (31916.6667,54733.3333), (31900.0,55133.3333), (31800.0,55700.0), (31816.6667,55966.6667), (31400.0,56366.6667), (31350.0,56633.3333), (32000.0,57300.0), (32016.6667,57333.3333), (32333.3333,57800.0), (32683.3333,58133.3333), (33600.0,57983.3333), (34466.6667,57716.6667), (34350.0,57433.3333), (34583.3333,55833.3333), (34600.0,55483.3333), (33933.3333,55683.3333), (33066.6667,55850.0), (33000.0,55783.3333), (33183.3333,55700.0), (33483.3333,56150.0), (33733.3333,56333.3333), (33750.0,56466.6667), (34800.0,56233.3333), (34905.0,56168.3333), (34742.2222,56098.3333), (34566.6667,55700.0), (33750.0,55283.3333), (33450.0,54533.3333), (33016.6667,53950.0), (32650.0,54250.0), (32466.6667,54316.6667), (32166.6667,55016.6667), (32466.6667,55233.3333), (32633.3333,55116.6667), (32383.3333,55066.6667), (32366.6667,54183.3333), (32350.0,54133.3333), (32950.0,54216.6667), (33250.0,54333.3333), (34733.6111,56036.6667), (34828.6111,56139.4444), (34801.6667,56334.1667), (34883.3333,56216.6667), (34883.3333,56200.0), (34909.7222,56152.2222), (34816.6667,56183.3333), (34605.0,56356.3889), (34533.3333,56300.0), (34189.1667,56339.4444), (34066.6667,56383.3333), (33600.0,56350.0), (32250.0,56516.6667), (31650.0,56833.3333), (30683.3333,57033.3333), (30166.6667,57100.0), (30250.0,56950.0), (30133.3333,57633.3333), (30733.3333,57316.6667), (31883.3333,57333.3333), (32250.0,57300.0), (32566.6667,56883.3333), (34066.6667,56300.0), (34250.0,55933.3333), (34350.0,55766.6667), (34366.6667,55783.3333), (34300.0,55966.6667), (34419.7222,56422.5), (34433.3333,57416.6667), (34333.3333,57716.6667), (34450.0,57600.0), (34400.0,57666.6667), (33600.0,57133.3333), (32483.3333,56350.0), (32183.3333,55283.3333), (31900.0,54783.3333), (31900.0,54150.0), (32016.6667,54200.0), (31966.6667,55050.0), (31783.3333,55150.0), (31350.0,55383.3333), (32383.3333,54350.0), (33233.3333,54383.3333), (33383.3333,55083.3333), (33600.0,55333.3333), (34000.0,55666.6667), (34050.0,55883.3333), (33950.0,55850.0), (34351.6667,56398.3333), (34290.5556,56388.8889), (34150.0,56950.0), (34316.6667,57000.0), (34300.0,57233.3333), (33450.0,57733.3333), (33100.0,57633.3333), (32883.3333,56800.0), (32216.6667,56016.6667), (32250.0,55750.0), (31916.6667,55933.3333), (31900.0,55883.3333), (32100.0,57416.6667), (32366.6667,57983.3333), (32750.0,57750.0), (32833.3333,57716.6667), (32916.6667,57733.3333), (33483.3333,55566.6667), (32666.6667,55450.0), (31300.0,55866.6667), (31233.3333,55883.3333), (31366.6667,55850.0), (31100.0,57016.6667), (31333.3333,57883.3333), (32100.0,57816.6667), (32516.6667,57750.0), (33133.3333,57150.0), (33850.0,56883.3333), (34411.6667,56402.2222), (34450.0,56283.3333), (34589.4444,56252.7778), (34633.3333,56333.3333), (34726.3889,56220.0), (34833.3333,56216.6667), (34875.0,56258.8889), (34885.2778,56060.5556), (34800.0,55233.3333), (34600.0,54550.0), (34116.6667,53950.0), (33616.6667,53716.6667), (33516.6667,53783.3333), (33250.0,53900.0), (33050.0,54150.0), (33100.0,55133.3333), (33416.6667,55633.3333), (32566.6667,57366.6667), (32850.0,57683.3333), (32933.3333,57650.0), (33183.3333,57466.6667), (34316.6667,57350.0), (33550.0,55666.6667), (33500.0,55216.6667), (33033.3333,57000.0), (33733.3333,57833.3333), (33716.6667,58266.6667), (33616.6667,58283.3333), (33950.0,58233.3333), (33716.6667,58083.3333), (33383.3333,57550.0), (32350.0,55833.3333), (32233.3333,55733.3333), (32050.0,55383.3333), (31766.6667,54800.0), (31800.0,54716.6667), (31500.0,54716.6667), (32150.0,54200.0), (32116.6667,54066.6667), (32200.0,54066.6667), (31733.3333,54416.6667), (31566.6667,54550.0), (31783.3333,54750.0), (31500.0,55166.6667), (31100.0,55666.6667), (31100.0,55983.3333), (31216.6667,56316.6667), (31300.0,57100.0), (31300.0,57700.0), (31333.3333,57833.3333), (31333.3333,57800.0), (31083.3333,57516.6667), (31416.6667,56683.3333), (31683.3333,56133.3333), (31850.0,56000.0), (32800.0,55800.0), (33083.3333,55966.6667), (33083.3333,56183.3333), (33300.0,56350.0), (34333.3333,57233.3333), (34066.6667,57350.0), (32766.6667,57783.3333), (32333.3333,58133.3333), (31300.0,57150.0), (31166.6667,57083.3333), (31283.3333,56433.3333), (31083.3333,56516.6667), (31116.6667,56466.6667), (31883.3333,57516.6667), (32016.6667,57466.6667), (32566.6667,57483.3333), (32383.3333,57600.0), (32500.0,56033.3333), (32450.0,55033.3333), (32633.3333,53900.0), (32783.3333,53833.3333), (33683.3333,53450.0), (33650.0,53800.0), (34033.3333,54283.3333), (34650.0,55233.3333), (34483.3333,55633.3333), (34666.6667,56000.0), (34781.1111,56053.3333), (34900.0,56133.3333), (34883.3333,56233.3333), (34400.0,56333.3333), (34366.6667,57066.6667), (33933.3333,57466.6667), (33816.6667,57550.0), (33083.3333,57433.3333), (32383.3333,57500.0), (32766.6667,57883.3333), (33544.1667,58197.2222), (34152.2222,58012.5), (33983.3333,58150.0), (34216.6667,57000.0), (34650.0,56716.6667), (34813.0556,56044.7222), (34666.6667,55266.6667), (34416.6667,56466.6667), (34383.3333,56383.3333), (32450.0,56033.3333), (32466.6667,56166.6667), (32383.3333,56683.3333), (31983.3333,57416.6667), (32000.0,57583.3333), (31350.0,57800.0), (31550.0,57950.0), (31350.0,57783.3333), (30400.0,56783.3333), (31383.3333,55866.6667), (31516.6667,55766.6667), (31816.6667,55183.3333), (32500.0,54416.6667), (33466.6667,54200.0), (33600.0,54316.6667), (33800.0,54000.0), (33000.0,55133.3333), (32533.3333,55500.0), (32083.3333,55650.0), (31183.3333,56283.3333), (31166.6667,57000.0), (31033.3333,56883.3333), (30433.3333,57433.3333), (30683.3333,57516.6667), (30833.3333,56750.0), (30750.0,56750.0), (30916.6667,56300.0), (31216.6667,55666.6667), (31233.3333,55633.3333), (31366.6667,55083.3333), (31483.3333,54833.3333), (31833.3333,54166.6667), (31866.6667,54200.0), (32000.0,54133.3333), (31783.3333,54333.3333), (32083.3333,54250.0), (32166.6667,54116.6667), (32350.0,53833.3333), (34266.6667,53933.3333), (34666.6667,54166.6667), (34966.6667,54950.0), (34483.3333,55650.0), (34450.0,56250.0), (34650.0,56750.0), (34583.8889,56699.4444), (34416.6667,57283.3333), (34316.6667,57216.6667), (34200.0,56983.3333), (33950.0,56750.0), (33383.3333,56416.6667), (33483.3333,56483.3333), (33413.0556,56500.5556), (32633.3333,56750.0), (30966.6667,55550.0), (30933.3333,55550.0), (31166.6667,55750.0), (31700.0,56100.0), (31750.0,56066.6667), (32416.6667,56333.3333), (32433.3333,56350.0), (32900.0,56083.3333), (33250.0,56016.6667), (34250.0,56683.3333), (34337.5,56713.6111), (34366.6667,57050.0), (34100.0,58000.0), (34033.3333,58133.3333), (34200.0,57866.6667), (33400.0,58316.6667), (33132.5,58295.5556), (33866.6667,57616.6667), (33850.0,57683.3333), (33583.3333,58083.3333), (33233.3333,57133.3333), (33250.0,57333.3333), (33050.0,56483.3333), (34095.5556,56214.1667), (34866.6667,56166.6667), (34833.3333,56116.6667), (34850.0,56083.3333), (34877.2222,56029.7222), (34550.0,55883.3333), (34633.3333,55966.6667), (34716.6667,55416.6667), (34800.0,55366.6667), (34716.6667,55533.3333), (34750.0,55683.3333), (34233.3333,55733.3333), (34183.3333,55733.3333), (34016.6667,57650.0), (33983.3333,57900.0), (33933.3333,58166.6667), (34350.0,57850.0), (34300.0,57733.3333), (34400.0,57166.6667), (34200.0,57100.0), (34521.9444,56393.6111), (34283.3333,56216.6667), (34366.6667,55516.6667), (34283.3333,55233.3333), (33850.0,55166.6667), (33466.6667,55616.6667), (32266.6667,55900.0), (31533.3333,56050.0), (30950.0,56650.0), (30616.6667,56900.0), (31083.3333,57600.0), (30966.6667,57533.3333), (31250.0,57200.0), (31783.3333,56250.0), (32883.3333,55516.6667), (33466.6667,54666.6667), (33666.6667,54200.0), (33683.3333,53550.0), (32750.0,53733.3333), (32566.6667,53416.6667), (32166.6667,53750.0), (32483.3333,53516.6667), (32583.3333,53383.3333), (32750.0,53483.3333), (32666.6667,53616.6667), (33016.6667,53700.0), (33000.0,53633.3333), (33216.6667,54383.3333), (33733.3333,54750.0), (33333.3333,54783.3333), (33166.6667,54966.6667), (32033.3333,55783.3333), (31883.3333,56000.0), (31833.3333,55983.3333), (33116.6667,55983.3333), (34450.0,55783.3333), (34761.6667,56223.6111), (34764.1667,56213.8889), (34370.0,55225.0), (34033.3333,55650.0), (33266.6667,55116.6667), (33266.6667,55100.0), (32300.0,55333.3333), (32166.6667,55950.0), (32066.6667,56350.0), (31633.3333,56916.6667), (31833.3333,57250.0), (31866.6667,57283.3333), (31883.3333,57483.3333), (32933.3333,55516.6667), (32533.3333,54566.6667), (32516.6667,54533.3333), (32383.3333,54666.6667), (31716.6667,55333.3333), (31683.3333,55433.3333), (31366.6667,55666.6667), (30866.6667,56366.6667), (30500.0,56450.0), (30483.3333,56516.6667), (31016.6667,56566.6667), (31033.3333,56600.0), (31466.6667,55166.6667), (31416.6667,54916.6667), (32066.6667,53766.6667), (32633.3333,53300.0), (33366.6667,53666.6667), (34200.0,53933.3333), (34166.6667,53850.0), (34166.6667,53833.3333), (32933.3333,54266.6667), (32216.6667,55600.0), (31516.6667,57533.3333), (31083.3333,57833.3333), (30783.3333,57783.3333), (30550.0,57866.6667), (31500.0,57116.6667), (31300.0,57066.6667), (31233.3333,57116.6667), (31300.0,57133.3333), (31616.6667,56816.6667), (31600.0,56750.0), (32533.3333,57133.3333), (33883.3333,56450.0), (33533.3333,54600.0), (33200.0,54750.0), (33466.6667,54650.0), (33866.6667,55550.0), (33883.3333,57400.0), (33866.6667,57516.6667), (33883.3333,57666.6667), (32416.6667,58150.0), (31950.0,57883.3333), (31916.6667,57716.6667), (31966.6667,57516.6667), (31250.0,56833.3333), (31183.3333,56933.3333), (30466.6667,56550.0), (30500.0,56666.6667), (30633.3333,56166.6667), (31516.6667,55966.6667), (31533.3333,55583.3333), (31550.0,55550.0), (32033.3333,54566.6667), (32616.6667,54600.0), (33133.3333,54933.3333), (34483.3333,54333.3333), (34900.0,54950.0), (34900.0,56150.0), (34883.3333,56183.3333), (34803.0556,56085.8333), (34700.0,55900.0), (34633.3333,55616.6667), (34500.0,55583.3333), (33516.6667,56400.0), (32683.3333,56883.3333), (32083.3333,56866.6667), (31666.6667,57916.6667), (31383.3333,57966.6667), (31350.0,57983.3333), (31083.3333,57016.6667), (31533.3333,55833.3333), (31816.6667,55500.0), (31983.3333,54166.6667), (32050.0,54633.3333), (32766.6667,55633.3333), (31583.3333,55466.6667), (31816.6667,54666.6667), (32150.0,54883.3333), (32983.3333,54583.3333), (32750.0,54400.0), (32516.6667,54583.3333), (32516.6667,54683.3333), (33833.3333,56300.0), (33550.0,56900.0), (33538.8889,56888.6111), (33533.3333,56900.0), (32321.3889,58075.5556), (32283.3333,58050.0), (32083.3333,57916.6667), (32616.6667,56483.3333), (32900.0,55233.3333), (33016.6667,55050.0), (33150.0,54150.0), (33050.0,54066.6667), (33200.0,53800.0), (33233.3333,53850.0), (32933.3333,53950.0), (32483.3333,53716.6667), (32100.0,53750.0), (32500.0,54016.6667), (34200.0,54750.0), (34800.0,54916.6667), (34733.3333,55266.6667), (34762.5,56020.5556), (34633.3333,56619.1667), (34400.0,56533.3333), (34442.2222,56443.6111), (34449.7222,56079.1667), (34333.3333,55650.0), (33933.3333,55266.6667), (34066.6667,54500.0), (32716.6667,55600.0), (32400.0,55350.0), (31600.0,55850.0), (32100.0,54866.6667), (32050.0,54866.6667), (30933.3333,55483.3333), (30900.0,55516.6667), (31450.0,55416.6667), (32016.6667,55066.6667), (32183.3333,55033.3333), (32266.6667,54916.6667), (33116.6667,54833.3333), (33466.6667,55116.6667), (34497.5,56037.2222), (34646.9444,56062.7778), (34200.0,56216.6667), (34166.6667,56683.3333), (33850.0,57016.6667), (33166.6667,57583.3333), (32983.3333,58050.0), (32416.6667,57583.3333), (32116.6667,57566.6667), (32400.0,56900.0), (32400.0,56716.6667), (32783.3333,55900.0), (32366.6667,54766.6667), (32150.0,55050.0), (31500.0,56033.3333), (31300.0,56016.6667), (31250.0,55950.0), (30733.3333,56733.3333), (31666.6667,56166.6667), (31983.3333,55683.3333), (32333.3333,55883.3333), (32333.3333,55966.6667), (31666.6667,56633.3333), (31450.0,56383.3333), (31083.3333,56016.6667), (31000.0,56250.0), (30300.0,56966.6667), (30600.0,57683.3333), (30233.3333,57583.3333), (30400.0,56466.6667), (31000.0,55683.3333), (32833.3333,54766.6667), (33400.0,54683.3333), (34866.6667,54866.6667), (34900.0,55283.3333), (34650.0,55866.6667), (34716.6667,55950.0), (34715.2778,56073.3333), (34600.0,56133.3333), (34533.3333,56316.6667), (34683.3333,56733.3333), (34763.3333,56385.2778), (34383.3333,56283.3333), (32833.3333,56433.3333), (32233.3333,56500.0), (31916.6667,57250.0), (31300.0,57200.0), (30566.6667,56883.3333), (30316.6667,56816.6667), (30250.0,56850.0), (31683.3333,55950.0), (32800.0,57050.0), (33333.3333,57950.0), (33883.3333,58416.6667), (33989.1667,58285.5556), (34200.0,57783.3333), (34433.3333,57716.6667), (34382.7778,56541.6667), (34500.0,56383.3333), (34450.0,56166.6667), (34433.3333,55983.3333), (34516.6667,55250.0), (34366.6667,54066.6667), (34366.6667,53833.3333), (34166.6667,54666.6667), (34522.7778,56277.7778), (34650.0,56600.0), (34366.6667,57566.6667), (34066.6667,57716.6667), (33966.6667,58283.3333), (33516.6667,57833.3333), (34183.3333,57933.3333), (33766.6667,58350.0), (32333.3333,57933.3333), (31583.3333,57616.6667), (31400.0,57783.3333), (31250.0,57166.6667), (31200.0,57233.3333), (32000.0,57166.6667), (32816.6667,56516.6667), (34133.3333,56400.0), (34858.0556,56170.8333), (34908.3333,56208.3333), (34816.6667,56100.0), (34900.0,56100.0), (34366.6667,55166.6667), (34283.3333,54983.3333), (34333.3333,55450.0), (34683.3333,55683.3333), (34766.6667,55750.0), (34860.2778,56052.2222), (34850.0,56116.6667), (34900.0,56183.3333), (34905.2778,56194.4444), (34922.7778,56159.7222), (34665.0,56219.4444), (33616.6667,57633.3333), (33650.0,57533.3333), (33750.0,57483.3333), (33900.0,55150.0), (33883.3333,54716.6667), (34050.0,54783.3333), (34266.6667,54316.6667), (34183.3333,53783.3333), (33883.3333,53500.0), (33566.6667,53850.0), (33250.0,53916.6667), (33266.6667,53783.3333), (33183.3333,53900.0), (33266.6667,54416.6667), (33533.3333,54433.3333), (34050.0,56200.0), (34083.3333,57383.3333), (34033.3333,57833.3333), (33800.0,58250.0), (33916.6667,57783.3333), (34283.3333,57616.6667), (34266.6667,57450.0), (33900.0,56833.3333), (32633.3333,56350.0), (32150.0,56116.6667), (31733.3333,55983.3333), (31516.6667,54966.6667), (31633.3333,55000.0), (31800.0,55333.3333), (32766.6667,55433.3333), (32416.6667,56166.6667), (32350.0,56550.0), (32150.0,54950.0), (32233.3333,54983.3333), (32966.6667,55400.0), (33483.3333,55150.0), (33350.0,55616.6667), (33200.0,56783.3333), (33533.3333,56933.3333), (33500.0,56750.0), (34366.6667,56400.0), (34698.3333,56217.5), (33333.3333,56466.6667), (32183.3333,56066.6667), (31833.3333,55933.3333), (31816.6667,55916.6667), (31883.3333,55966.6667), (31766.6667,56250.0), (32933.3333,57116.6667), (33750.0,57616.6667), (33883.3333,57383.3333)]
    converted_data = process_data(tourneydata)
    plot(converted_data)