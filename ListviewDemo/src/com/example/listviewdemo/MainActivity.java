
package com.example.listviewdemo;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;


import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.widget.ListView;
import android.widget.SimpleAdapter;

public class MainActivity extends Activity {

    ListView listContent1;
    ListView listContent2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        listContent1 = (ListView)findViewById(R.id.listView1);
        listContent2 = (ListView)findViewById(R.id.listView2);
        initContentList("test");
        initContentList2("test");
    }
    
    public void initContentList(String MenuItem){
        List<HashMap<String, String>> list = new ArrayList<HashMap<String, String>>();
        for (int i = 0; i < 15; i++) {
            HashMap<String, String> map = new HashMap<String, String>();
            map.put("title", MenuItem + i);
            map.put("title1",
                    "初始化数据。向listview中添加隐藏的文本内容");
            list.add(map);
        }
        SimpleAdapter adapter = new SimpleAdapter(this, list, R.layout.main_category_content_item_text,
                new String[] { "title", "title1" }, new int[] { R.id.text1,
                        R.id.text2 });
        listContent1.setAdapter(adapter);
    }

    public void initContentList2(String MenuItem){
        List<HashMap<String, String>> list = new ArrayList<HashMap<String, String>>();
        for (int i = 0; i < 15; i++) {
            HashMap<String, String> map = new HashMap<String, String>();
            map.put("title", MenuItem + i);
            map.put("title1",
                    "初始化数据。向listview中添加隐藏的文本内容");
            list.add(map);
        }
        SimpleAdapter adapter = new SimpleAdapter(this, list, R.layout.main_category_content_item_text,
                new String[] { "title", "title1" }, new int[] { R.id.text1,
                        R.id.text2 });
        listContent2.setAdapter(adapter);
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

}
