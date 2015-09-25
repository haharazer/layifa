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
        $pageSize = 16;
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
                    'title' => array(
                        'query' => $query,
                        'minimum_should_match' => '75%',
                    )
                ),
            ),
            'sort' => array(
                'created_at' => array(
                    'order' => 'desc',
                ),
            ),
            'from' => $offset,
            'size' => $pageSize,
        );
        $results = $client->search($searchParams);
        $items = array_map(function($item) {
            return (object)$item['_source'];
        }, $results['hits']['hits']);

        return view('search', ['title' => '搜索', 'items'=> $items, 'page' => $page, 'query' => $query]);
    }
} 