import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:dashboard/asset_data.dart';
import 'package:dashboard/asset_data_repository.dart';
import 'package:dashboard/daily_value.dart';

class FirestoreDataStore implements AssetDataRepository {
  @override
  Future<List<AssetData>> query() async {
    final assets = await FirebaseFirestore.instance.collection("assets").get();
    return AssetsParser(assets.docs.map((e) => e.data())).toAssetData();
  }
}

class AssetsParser {
  final Iterable<Map<String, dynamic>> _data;
  AssetsParser(this._data);
  List<AssetData> toAssetData() {
    final List<AssetData> assets = List.empty(growable: true);
    for (var e in _data) {
      final name = e['name'];
      final value = DailyParser(e).value;
      if (assets.any((a) => a.name == name)) {
        assets.firstWhere((e) => e.name == name).data.add(value);
      } else {
        assets.add(AssetData(name, List.of([value], growable: true)));
      }
    }
    return assets.toList(growable: false);
  }
}

class DailyParser {
  final DailyValue _value;
  DailyValue get value => _value;
  DailyParser(Map<String, dynamic> data)
      : _value = DailyValue(data['time'], data['value']);
}
