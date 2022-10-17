import 'package:dashboard/asset_data.dart';
import 'package:dashboard/asset_data_repository.dart';

import '../daily_value.dart';

class SampleRepository implements AssetDataRepository {
  @override
  Future<List<AssetData>> query() async {
    return [
      AssetData("Stocks - US", [
        DailyValue('2022-10-14 19:38:13', 1010),
        DailyValue('2022-10-13 19:38:13', 1000),
        DailyValue('2022-10-12 19:38:13', 900),
        DailyValue('2022-10-11 19:38:13', 1100),
        DailyValue('2022-10-10 19:38:13', 950)
      ]),
      AssetData("Stocks - Tokyo", [
        DailyValue('2022-10-14 19:38:13', 950),
        DailyValue('2022-10-10 19:38:13', 950),
        DailyValue('2022-10-12 19:38:13', 810),
        DailyValue('2022-10-11 19:38:13', 1000),
        DailyValue('2022-10-13 19:38:13', 900)
      ])
    ];
  }
}
