<?php
/**
 * Created by PhpStorm.
 * User: MyPC
 * Date: 2015/8/15
 * Time: 22:17
 */

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use DB;
use Elasticsearch;

class SearchController extends Controller {
    public static function index(Request $request)
    {
        $query = $request->input('query');
        $page = $request->input('page', 1);
        $pageSize = 12;
        $offset = ($page - 1) * $pageSize;

        $params = array();
        $params['hosts'] = array('106.185.25.253:9200');
        $client = new Elasticsearch\Client($params);
        $searchParams = array(
            'index' => 'youhui',
            'type' => 'jdbc',
        );
        $searchParams['body'] = array(
            'query' => array(
                'match' => array(
                    'title' => $query,
                ),
            ),
        );
        $results = $client->search($searchParams);
        $items = array_map(function($item) {
            return $item['_source'];
        }, $results['hits']['hits']);

        return view('search', ['title' => '搜索', 'items'=> $items, 'page' => $page, 'query' => $query]);
    }
} 