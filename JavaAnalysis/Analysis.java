import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Analysis {

  private static List<Double> AccList = Arrays.asList(0.015563965,0.018981934,0.019348145,0.022399902,0.016357422,0.019348145,0.018310547,0.012268066,0.01361084,0.012512207,0.013916016,0.0138549805,0.013366699,0.01184082,0.012145996,0.013305664,0.013671875,0.014892578,0.012390137,0.012329102,0.013366699,0.010986328,0.010314941,0.013305664,0.01586914,0.016418457,0.015075684,0.014465332,0.014587402,0.015563965,0.015991211,0.016174316,0.015136719,0.0178833,0.015808105,0.017150879,0.017150879,0.018127441,0.017578125,0.01953125,0.019592285,0.021118164,0.020874023,0.022583008,0.019348145,0.020080566,0.0211792,0.019592285,0.017333984,0.018371582,0.015319824,0.017028809,0.014709473,0.014587402,0.014709473,0.0138549805,0.0134887695,0.012756348,0.013366699,0.012023926,0.012878418,0.012329102,0.014526367,0.013977051,0.0154418945,0.01550293,0.015991211,0.015319824,0.015625,0.015930176,0.018310547,0.017211914,0.01953125,0.020019531,0.020874023,0.021606445,0.020385742,0.020141602,0.019165039,0.018188477,0.016723633,0.016723633,0.015197754);

  private static List<Double> HigherList = new ArrayList();
  private static List<Double> LowerList = new ArrayList();

  private static double LineOfBestFits;
  private static double arrayVal;
  private static double higherListMean;
  private static double lowerListMean;
  private static double difference;

  public static void main(String[] args) {
    difference = differenceFinder(AccList);

    System.out.println(difference);
  }

  public static double differenceFinder(List<Double> list) {
    LineOfBestFits = FindMean(list);
    
    for (int i = 0; i < list.size(); i++) {
      arrayVal = list.get(i);
      if (arrayVal > LineOfBestFits) {
        HigherList.add(arrayVal);
      } else {
        LowerList.add(arrayVal);
      }
    }

    higherListMean = FindMean(HigherList);
    lowerListMean = FindMean(LowerList);

    difference = higherListMean - lowerListMean;

    return difference;
  }

  public static double FindMean(List<Double> list) {
    double meanOfList = list.stream().mapToDouble(val -> val).average().orElse(0.0);
    return meanOfList;
  }
}