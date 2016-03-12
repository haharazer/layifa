<?php
/**
 * Created by PhpStorm.
 * User: MyPC
 * Date: 2015/8/15
 * Time: 22:17
 */

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use DB;
use Elasticsearch;

class SearchController extends Controller {
    public static function index(Request $request)
    {
        $query = $request->input('query');

        $items = DB::table('discounts')
            ->where('tag', 'like', "%$query%")
            ->orderBy('created_at', 'desc')
            ->paginate(12);

        return view('search', ['title' => '搜索', 'items'=> $items, 'query' => $query]);
    }
} 